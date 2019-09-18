import {throttle} from '../throttle/throttle';
import {KEY_CODES} from '../../constants/key-codes';

export const DATA_ATTRS = {
  API_ENDPOINT: 'data-api-endpoint',
  NO_RESULTS: 'data-no-results',
  RESULT: 'data-result',
  SID: 'data-sid',
};

export const FUZZY_CONSTS = {
  INPUT: {
    CLASS: 'dmb-fuzzy-search__input',
    ATTR: 'dmb-fuzzy-search-input',
  },
  RESULTS: {
    CLASS: 'dmb-fuzzy-search__results',
    ATTR: 'dmb-fuzzy-search-results',
  },
  RESULTS_COUNT: {
    ATTR: 'dmb-fuzzy-search-results-count',
  },
  RESULTS_LIST: {
    CLASS: 'dmb-fuzzy-search__results-list',
    ATTR: 'dmb-fuzzy-search-results-list',
  },
  RESULT_ITEM: {
    CLASS: 'dmb-fuzzy-search__result-item',
    ATTR: 'dmb-fuzzy-search-result-item',
  },
  RESULT_ITEM_HEADING: {
    CLASS: 'dmb-fuzzy-search__result-item-heading',
  },
  RESULT_ITEM_SUBHEADING: {
    CLASS: 'dmb-fuzzy-search__result-item-subheading',
  },
  ERROR: {
    ATTR: 'dmb-fuzzy-search-server-error',
  },
};

export const SELECTED_EVENT = 'selectResult';

/**
 * Fuzzy search component
 *
 */
export default class FuzzySearch {
  /**
   * Attaches methods to provided element
   *
   * @param {Node} elem : Element to attach fuzzy search functionality to
   */
  constructor(elem) {
    this.elem = elem;

    this.results = [];
    this.resultsCount = null;
    this.selectedResultIndex = null;

    // Get DOM elements
    this.searchInputEl = elem.querySelector(`[${FUZZY_CONSTS.INPUT.ATTR}]`);
    this.resultsEl = elem.querySelector(`[${FUZZY_CONSTS.RESULTS.ATTR}]`);
    this.resultsCountEl = this.resultsEl.querySelector(`[${FUZZY_CONSTS.RESULTS_COUNT.ATTR}]`);
    this.resultsListEl = this.resultsEl.querySelector(`[${FUZZY_CONSTS.RESULTS_LIST.ATTR}]`);
    this.serverErrorEl = elem.querySelector(`[${FUZZY_CONSTS.ERROR.ATTR}]`);

    // Get search API endpoint
    this.apiEndpoint = elem.getAttribute(DATA_ATTRS.API_ENDPOINT);

    // Methods
    this.search = this.search.bind(this);
    this.handleInput = this.handleInput.bind(this);
    this.handleKeydown = this.handleKeydown.bind(this);
    this.handleClick = this.handleClick.bind(this);

    this.throttledSearch = throttle(this.search, 300);


    // Attach event listeners
    this.searchInputEl.addEventListener('input', this.handleInput);
    this.searchInputEl.addEventListener('keydown', this.handleKeydown);
    this.resultsEl.addEventListener('click', this.handleClick);
  }


  /**
   * Handle input in search box
   *
   * @param {Event} e : Event
   *
   */
  handleInput(e) {
    const query = e.target.value;
    if (query.length === 0) {
      this.clearResults();
      return;
    }

    this.throttledSearch(query);
  }

  /**
   * Handle click event in search box
   *
   * @param {Event} e : Event
   *
   */
  handleClick(e) {
    if (!e.target) {
      return;
    }

    const selectedResultItemEl = e.target.closest(`[${FUZZY_CONSTS.RESULT_ITEM.ATTR}]`);

    if (selectedResultItemEl) {
      const index = [...selectedResultItemEl.parentElement.children].indexOf(selectedResultItemEl);
      this.selectHandler(index);
    }
  }


  /**
   * Attaches FuzzySearch functionality to element
   *
   * @param {Node} elem : Element to attach FuzzySearch to
   * @return {FuzzySearch} : Returns a reference to the FuzzySearch instance created
   */
  static attachTo(elem) {
    return new FuzzySearch(elem);
  }


  /**
   * Handles the keydown event, changing the selected results with
   * the up/down arrows and selects the result on Enter key
   *
   * @param {Event} e : Event
   */
  handleKeydown(e) {
    // If up or down arrow key pressed determine which element to set as selected
    const keyCode = e.keyCode ? e.keyCode : e.which;

    if (!(keyCode === KEY_CODES.UP || keyCode == KEY_CODES.DOWN || keyCode == KEY_CODES.ENTER)) {
      return;
    }

    e.preventDefault();

    // Get currently selected element
    const selectedResult = this.resultsEl.querySelector('[aria-selected="true"]');

    // If Enter key pressed run selectHandler
    if (keyCode == KEY_CODES.ENTER) {
      if (!selectedResult) {
        return;
      }

      this.selectHandler(this.selectedResultIndex);
      return;
    }

    // Get number of elements in DOM
    // const resultsCount = parseInt(this.resultsEl.getAttribute('data-results-count'), 10);

    // If less than two elements ignore arrow keys
    if (!this.resultsCount || this.resultsCount < 2) {
      return;
    }

    // Unselect currently selected element
    selectedResult.setAttribute('aria-selected', 'false');

    if (keyCode == KEY_CODES.DOWN) {
      // If down arrow key pressed select next item in list
      // or loop back to first item from last item
      this.selectedResultIndex++;

      if (this.selectedResultIndex === this.resultsCount) {
        this.selectedResultIndex = 0;
      }
    } else if (keyCode == KEY_CODES.UP) {
      // If up arrow key pressed select previous item in list
      // or loop to last item from first item
      this.selectedResultIndex--;

      if (this.selectedResultIndex < 0) {
        this.selectedResultIndex = this.resultsCount - 1;
      }
    }

    // Set aria-selected of selected element to true
    const selectedResultEl = this.resultsListEl.childNodes[this.selectedResultIndex];

    selectedResultEl.setAttribute('aria-selected', 'true');

    // Scroll to element in list
    selectedResultEl.scrollIntoView({
      behaviour: 'smooth',
      block: 'nearest',
      inline: 'start',
    });
  }


  /**
   * Searches for results using the endpoint in the component's
   * 'data-api-endpoint' attribute as '/api/${this.apiEndpoint}'
   *
   * @param {string} query : Search query
   */
  search(query) {
    // encode search query
    const encodedQuery = encodeURI(query);

    // Search using given API endpoint and query
    fetch(`/api/${this.apiEndpoint}?q=${encodedQuery}`)
      .then((resp) => {
        if (resp.status !== 200) {
          return Promise.reject(`HTTP error status code: ${resp.status}`);
        }
        return resp.json();
      })
      .then((results) => {
        if (this.searchInputEl.value !== query) {
          return;
        }

        this.results = results;
        this.resultsCount = results.length;

        this.renderResults();
      })
      .catch(() => {
        this.serverErrorEl.style.display = 'block';
      });
  }


  /**
   * Render the results to in the view
   *
   * @param {Array.<Object>} results
   */
  renderResults() {
    // Update the results count element
    if (this.resultsCount === 0) {
      this.resultsListEl.innerHTML = '';
      this.resultsCountEl.textContent = this.resultsCountEl
        .getAttribute(DATA_ATTRS.NO_RESULTS);
    }

    if (this.resultsCount !== 0) {
      this.resultsCountEl.textContent =
        `${this.resultsCount} result${this.resultsCount === 1 ? '' : 's'}`;

      // Create temporary element to store results list item elements
      const tempEl = this._createEl(
        'ul',
        FUZZY_CONSTS.RESULTS_LIST.CLASS
      );

      tempEl.setAttribute(FUZZY_CONSTS.RESULTS_LIST.ATTR, '');

      this.results.forEach((result, index) => {
        const resultItemEl = this._createEl(
          'li',
          FUZZY_CONSTS.RESULT_ITEM.CLASS
        );

        const companyNameEl = this._createEl(
          'div',
          FUZZY_CONSTS.RESULT_ITEM_HEADING.CLASS,
          `${result['company_name']}`
        );

        const accountIdEl = this._createEl(
          'div',
          `${FUZZY_CONSTS.RESULT_ITEM_SUBHEADING.CLASS} dmb-u-small-text dmb-u-text-muted`,
          `
            ${result['account_id'] ? result['account_id'] : '\u200B'}
            ${result['account_id'] ? '\u2022' : '\u200B'}
            ${result['country_name']}
          `
        );

        resultItemEl.setAttribute(FUZZY_CONSTS.RESULT_ITEM.ATTR, '');
        resultItemEl.setAttribute(FUZZY_CONSTS.RESULT_ITEM.ATTR, '');
        resultItemEl.setAttribute('role', 'option');

        resultItemEl.setAttribute(DATA_ATTRS.RESULT, JSON.stringify(result));

        // Set first result as selected
        if (index === 0) {
          resultItemEl.setAttribute('aria-selected', 'true');
        }

        resultItemEl.appendChild(companyNameEl);
        resultItemEl.appendChild(accountIdEl);

        tempEl.appendChild(resultItemEl);
      });

      this.resultsListEl.parentNode.replaceChild(
        tempEl,
        this.resultsListEl
      );
      this.resultsListEl = tempEl;

      this.selectedResultIndex = 0;
    }

    // Show the results list if hidden
    if (this.resultsEl.style.display !== 'block') {
      this.resultsEl.style.display = 'block';
    }
  }


  /**
   * Handle when a result is selected by firing custom selectResult event
   *
   * @param {number} selectedResultIndex
   */
  selectHandler(selectedResultIndex) {
    const event = new CustomEvent('selectResult', {detail: this.results[selectedResultIndex]});
    window.dispatchEvent(event);
  }


  /**
   * Clears all resultsListEl's and hides resultsEl
   *
   */
  clearResults() {
    this.resultsCount = 0;
    this.resultsListEl.innerHTML = '';
    this.resultsEl.style.display = 'none';
  }


  /**
   * Creates an element with a class and optional text content
   *
   * @param {string} type : Element type (div, h1, li, etc)
   * @param {string} className : Element class
   * @param {string=} textContent : Element text content
   *
   * @return {Element} : Return the created element
   */
  _createEl(type, className, textContent) {
    const elem = document.createElement(type);
    elem.setAttribute('class', className);

    if (textContent) {
      elem.textContent = textContent;
    }

    return elem;
  }
}

import {throttle} from '../throttle/throttle';

/**
 *
 * Usage:
 *
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

    this.selectedResultIndex = null;

    // Get DOM elements
    this.searchInputEl = elem.querySelector('.dmb-fuzzy-search__input');
    this.resultsEl = elem.querySelector('.dmb-fuzzy-search__results');
    this.resultsCountEl = this.resultsEl.querySelector('.dmb-fuzzy-search__results-count');

    // Get API endpoint
    this.apiEndpoint = elem.getAttribute('data-api-endpoint');

    // Attach event listeners
    this.searchInputEl.addEventListener(
      'input',
      throttle(
        (e) => {
          const query = e.target.value;
          if (query.length === 0) {
            this.clearResults();
            return;
          }
          return this.search(query);
        },
        1000
      )
    );

    this.searchInputEl.addEventListener('keydown', (e) => this.handleKeydown(e));

    this.resultsEl.addEventListener('click', (e) => {
      if (e.target && e.target.className.includes('dmb-fuzzy-search__result-item')) {
        const sid = e.target.getAttribute('data-sid');
        this.selectHandler(sid);
      }
    });
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

    if (!(keyCode == 38 || keyCode == 40 || keyCode == 13)) {
      return;
    }

    e.preventDefault();

    // Get currently selected element
    const selectedResult = this.resultsEl.querySelector('[aria-selected="true"]');

    // If Enter key pressed run selectHandler
    if (keyCode == 13) {
      if (!selectedResult) {
        return;
      }

      this.selectHandler(selectedResult.getAttribute('data-sid'));
      return;
    }

    // Get number of elements in DOM
    const resultsCount = parseInt(this.resultsEl.getAttribute('data-results-count'), 10);

    // If less than two elements ignore arrow keys
    if (resultsCount < 2 || !resultsCount) {
      return;
    }

    // Unselect currently selected element
    selectedResult.setAttribute('aria-selected', 'false');

    if (keyCode == 40) {
      // If down arrow key pressed select next item in list
      // or loop back to first item from last item
      this.selectedResultIndex++;

      if (this.selectedResultIndex === resultsCount) {
        this.selectedResultIndex = 0;
      }
    } else if (keyCode == 38) {
      // If up arrow key pressed select previous item in list
      // or loop to last item from first item
      this.selectedResultIndex--;

      if (this.selectedResultIndex < 0) {
        this.selectedResultIndex = resultsCount - 1;
      }
    }

    // Set aria-selected of selected element to true
    const resultsListEl = this.resultsEl.querySelector('.dmb-fuzzy-search__results-list');
    const selectedResultEl = resultsListEl.childNodes[this.selectedResultIndex];

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

        this.renderResults(results);
      })
      .catch((err) => {
        console.error(`Error: `, err);
      });
  }


  /**
   * Render the results to in the view
   *
   * @param {Array.<Object>} results
   */
  renderResults(results) {
    const resultsListEl = this.resultsEl
      .querySelector('.dmb-fuzzy-search__results-list');

    this.resultsEl.setAttribute(
      'data-results-count',
      results.length
    );

    // Update the results count element
    if (results.length === 0) {
      resultsListEl.innerHTML = '';
      this.resultsCountEl.textContent = this.resultsCountEl
        .getAttribute('data-no-results');
    }

    if (results.length !== 0) {
      this.resultsCountEl.textContent =
        `${results.length} result${results.length === 1 ? '' : 's'}`;

      // Create temporary element to store
      // results list item elements
      const tempEl = this._createEl(
        'ul',
        'dmb-fuzzy-search__results-list'
      );

      results.forEach((result, index) => {
        const resultsListItemEl = this._createEl(
          'li',
          'dmb-fuzzy-search__result-item'
        );

        const companyNameEl = this._createEl(
          'div',
          'dmb-fuzzy-search__result-item-heading',
          `${result['company_name']}`
        );

        const accountIdEl = this._createEl(
          'div',
          'dmb-fuzzy-search__result-item-subheading dmb-u-small-text dmb-u-text-muted',
          `${result['account_id'] ? result['account_id'] : '\u200B'}`
        );

        resultsListItemEl.setAttribute(
          'data-sid',
          `${result['sid']}`
        );

        resultsListItemEl.setAttribute('role', 'option');

        // Set first result as selected
        if (index === 0) {
          resultsListItemEl.setAttribute('aria-selected', 'true');
        }

        resultsListItemEl.appendChild(companyNameEl);
        resultsListItemEl.appendChild(accountIdEl);

        tempEl.appendChild(resultsListItemEl);
      });

      resultsListEl.parentNode.replaceChild(
        tempEl,
        resultsListEl
      );

      this.selectedResultIndex = 0;
    }

    // Show the results list if hidden
    if (window.getComputedStyle(this.resultsEl, null).display === 'none') {
      this.resultsEl.style.display = 'block';
    }
  }


  /**
   * Handle when a result is selected
   *
   * @param {string} sid
   */
  selectHandler(sid) {
    console.log(sid);
  }


  /**
   * Clears all resultsListEl's and hides resultsEl
   *
   */
  clearResults() {
    this.resultsEl.querySelector('.dmb-fuzzy-search__results-list').innerHTML = '';
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

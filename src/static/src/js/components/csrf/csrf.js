const csrfTokenElement = document.querySelector('[name="csrfmiddlewaretoken"]');
export const csrfToken = csrfTokenElement ? csrfTokenElement.value : '';

let bootstrapData;
try {
  const bootstrapDatString = document.querySelector('[data-bootstrap-data]').dataset['bootstrapData'];
  bootstrapData = bootstrapDatString ? JSON.parse(bootstrapDatString) : {};
} catch (e) {
  console.warn('Not valid json');
}
export {bootstrapData};

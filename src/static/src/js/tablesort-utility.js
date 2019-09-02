export const configureAdditionalSortTypes = ['glueTableSortServiceProvider', function(glueTableSortServiceProvider) {
  glueTableSortServiceProvider.setSortType('datetime-custom', function(a, b) {
    const dateA = Date.parse(a.trim().split('utc=')[1]);
    const dateB = Date.parse(b.trim().split('utc=')[1]);

    return dateB < dateA ? 1 : -1;
  });

  glueTableSortServiceProvider.setDefaultSortTypes();
}];

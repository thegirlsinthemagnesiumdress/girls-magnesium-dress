const eventsTemplate = `
    <ul class="aa-events__list">
        {{#each futureEvents}}
            {{> event }}
        {{/each}}
    </ul>
    <h3 class="aa-events__past-title"> Past events</h3>
    <ul class="aa-events__list">
    {{#each pastEvents}}
        {{> event }}
    {{/each}}
    </ul>

`;

export default eventsTemplate;
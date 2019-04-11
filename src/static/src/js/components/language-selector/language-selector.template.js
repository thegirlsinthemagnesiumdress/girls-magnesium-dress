goog.module('dmb.components.languageSelector.template');

const template = `
<form id="language-form" action="{[url]}" method="post" >
    <select name="language" ng-model="lang" ng-change="languageSelectorCtrl.changeLanguage()">
        <option
                ng-repeat="language in languages"
                value="{[language.code]}
                ng-selected="language.code == selectedLanguage">
            {[ language.name_local ]}
        </option>
    </select>
    
</form>
`;

exports = template;
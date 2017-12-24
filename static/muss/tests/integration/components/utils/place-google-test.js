import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';

moduleForComponent('utils/place-google', 'Integration | Component | utils/place google', {
  integration: true
});

test('it renders', function(assert) {
  // Set any properties with this.set('myProperty', 'value');
  // Handle any actions with this.on('myAction', function(val) { ... });

  this.render(hbs`{{utils/place-google}}`);

  assert.equal(this.$().text().trim(), '');

  // Template block usage:
  this.render(hbs`
    {{#utils/place-google}}
      template block text
    {{/utils/place-google}}
  `);

  assert.equal(this.$().text().match(/template block text/), 'template block text');
});

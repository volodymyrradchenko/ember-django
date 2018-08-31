import Component from '@ember/component';
import { task } from 'ember-concurrency';

export default Component.extend({
	model: null,

	deletePost: task(function* () {
		yield this.model.destroyRecord();
	})
});

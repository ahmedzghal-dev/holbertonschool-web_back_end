const calculateNumber = require("./0-calcul.js");
const mocha = require("mocha");
const assert = require("assert");

describe("calculateNumber", () => {
	it("returns rounded sum", () => {
		assert.strictEqual(calculateNumber(2, 5), 7);
		assert.strictEqual(calculateNumber(2.7, 6), 9);
		assert.strictEqual(calculateNumber(2.2, 5.7), 8);
		assert.strictEqual(calculateNumber(-2, -1), -3);
		assert.strictEqual(calculateNumber(-2.4, -5.7), -8);
	});
	it("should throw error if NaN passed", function () {
		assert.throws(() => calculateNumber(NaN, 7), "[Function: TypeError]");
	});
});
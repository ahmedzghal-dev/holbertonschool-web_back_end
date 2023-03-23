export default class Currency {
    constructor(code, name) {
      this._name = name;
      this._code = code;
    }
  
    get code() {
      return this._code;
    }
  
    get name() {
      return this._name;
    }
  
    set code(value) {
      this._code = value;
    }
  
    set name(value) {
      this._name = value;
    }
  
    displayFullCurrency() {
      return `${this._name} (${this._code})`;
    }
  }
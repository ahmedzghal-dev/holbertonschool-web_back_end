export default class Pricing {
    constructor(amount, currency) {
      if (typeof (amount) !== 'number') throw TypeError('must be a number');
      this._amount = amount;
      this._currency = currency;
    }
  
    get amount() {
      return this._amount;
    }
  
    get currency() {
      return this._currency;
    }
  
    set amount(value) {
      this._amount = value;
    }
  
    set name(value) {
      this._currency = value;
    }
  
    displayFullPrice() {
      return `${this._amount} ${this._currency.displayFullCurrency()}`;
    }
  
    static convertPrice(amount, conversionRate) {
      return amount * conversionRate;
    }
  }
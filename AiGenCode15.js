// A class representing a Bank Account
class BankAccount {
  constructor(accountNumber, accountHolderName) {
    this.accountNumber = accountNumber;
    this.accountHolderName = accountHolderName;
    this.balance = 0;
    this.transactions = [];
  }

  // Deposits funds into the account
  deposit(amount) {
    if (amount > 0) {
      this.balance += amount;
      this.transactions.push(`Deposited: £${amount}`);
    } else {
      console.log("Invalid deposit amount.");
    }
  }

  // Withdraws funds from the account
  withdraw(amount) {
    if (amount > 0 && amount <= this.balance) {
      this.balance -= amount;
      this.transactions.push(`Withdrew: £${amount}`);
    } else {
      console.log("Insufficient balance or invalid withdrawal amount.");
    }
  }

  // Displays account details and transactions
  displayDetails() {
    console.log(`Account Number: ${this.accountNumber}`);
    console.log(`Account Holder Name: ${this.accountHolderName}`);
    console.log(`Current Balance: £${this.balance.toFixed(2)}`);
    console.log("Transaction History:");
    this.transactions.forEach((transaction, index) => {
      console.log(`${index + 1}. ${transaction}`);
    });
  }
}

// Example usage:
const account = new BankAccount("1234567890", "John Doe");
account.deposit(100);
account.withdraw(50);
account.displayDetails();

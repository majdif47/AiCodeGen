// Define a struct to represent a Bank Account
#[derive(Debug, PartialEq)]
struct BankAccount {
    account_number: String,
    balance: f64,
}

impl BankAccount {
    // Create a new bank account with initial balance
    fn new(account_number: String, initial_balance: f64) -> Self {
        Self {
            account_number,
            balance: initial_balance,
        }
    }

    // Deposit money into the account
    fn deposit(&mut self, amount: f64) -> bool {
        if amount > 0.0 {
            self.balance += amount;
            true
        } else {
            false
        }
    }

    // Withdraw money from the account
    fn withdraw(&mut self, amount: f64) -> bool {
        if amount > 0.0 && amount <= self.balance {
            self.balance -= amount;
            true
        } else {
            false
        }
    }

    // Display account information
    fn display_info(&self) {
        println!("Account Number: {}", self.account_number);
        println!("Current Balance: ${}", self.balance);
    }
}

fn main() {
    // Create a new bank account with initial balance
    let mut account = BankAccount::new("1234567890".to_string(), 1000.0);

    // Deposit money into the account
    if account.deposit(500.0) {
        println!("Deposited $500.00 successfully.");
    } else {
        println!("Invalid deposit amount.");
    }

    // Withdraw money from the account
    if account.withdraw(200.0) {
        println!("Withdrew $200.00 successfully.");
    } else {
        println!("Insufficient funds for withdrawal.");
    }

    // Display account information
    account.display_info();

    // Update balance with interest
    account.balance += 100.0;
    account.display_info();
}

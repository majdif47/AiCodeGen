// A simple implementation of a Bank Account system.

struct Transaction {
    amount: f64,
    description: String,
}

enum Event {
    Deposit(f64, String),
    Withdrawal(f64, String),
    Balance inquiry,
}

struct BankAccount {
    balance: f64,
}

impl BankAccount {
    fn new() -> Self {
        Self { balance: 0.0 }
    }

    fn deposit(&mut self, amount: f64, description: String) {
        if amount < 0.0 {
            panic!("Deposit amount cannot be negative.");
        }
        self.balance += amount;
        println!("Deposited ${} for {}", amount, description);
    }

    fn withdraw(&mut self, amount: f64, description: String) {
        if amount < 0.0 || amount > self.balance {
            panic!("Insufficient funds or deposit amount cannot be negative.");
        }
        self.balance -= amount;
        println!("Withdrew ${} for {}", amount, description);
    }

    fn balance(&self) -> f64 {
        self.balance
    }
}

struct BankSystem {
    accounts: Vec<BankAccount>,
}

impl BankSystem {
    fn new() -> Self {
        Self { accounts: vec![] }
    }

    fn add_account(&mut self) {
        let account = BankAccount::new();
        self.accounts.push(account);
        println!("Account created with ID 1");
    }

    fn get_account(&self, id: usize) -> Option<&BankAccount> {
        self.accounts.get(id)
    }

    fn get_balance(&self, id: usize) -> f64 {
        match self.get_account(id) {
            Some(account) => account.balance(),
            None => 0.0,
        }
    }

    fn deposit_event(&mut self, id: usize, amount: f64, description: String) {
        if let Some(account) = self.get_account(id) {
            account.deposit(amount, description);
        } else {
            println!("Account with ID {} does not exist.", id);
        }
    }

    fn withdraw_event(&mut self, id: usize, amount: f64, description: String) {
        if let Some(account) = self.get_account(id) {
            account.withdraw(amount, description);
        } else {
            println!("Account with ID {} does not exist.", id);
        }
    }

    fn balance_inquiry_event(&mut self, id: usize) {
        if let Some(account) = self.get_account(id) {
            println!("Account Balance for ID {}: ${}", id, account.balance());
        } else {
            println!("Account with ID {} does not exist.", id);
        }
    }
}

fn main() {
    let mut bank_system = BankSystem::new();

    // Add accounts
    bank_system.add_account();
    bank_system.add_account();

    // Deposit and withdraw money from an account
    bank_system.deposit_event(1, 100.0, "Salary");
    bank_system.withdraw_event(1, 50.0, "Rent");

    // Check balance of a specific account
    println!("Balance for ID 1: ${}", bank_system.get_balance(1));

    // Handle events on an existing account
    bank_system.deposit_event(1, 200.0, "Bonus");
    bank_system.withdraw_event(1, 150.0, "Car Payment");

    // Perform a balance inquiry on a non-existent account
    println!("Balance for ID 3: ${}", bank_system.get_balance(3));

    // Perform events on multiple accounts
    for i in (0..2) {
        bank_system.deposit_event(i + 1, 500.0 + i as f64 * 100.0, format!("Salary {}", i));
        bank_system.withdraw_event(i + 1, 200.0 + i as f64 * 50.0, format!("Rent {}", i));
    }

    // Perform events on all accounts
    for account in &mut bank_system.accounts {
        bank_system.deposit_event(2, 1000.0, "Bonus");
        bank_system.withdraw_event(2, 500.0, "Insurance");
    }
}

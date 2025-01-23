package main

import (
    "fmt"
    "math/rand"
    "time"
)

// Simulates a Bank Account with transactions
type Transaction struct {
    Type     string `enum:"Deposited,Withdrawn"`
    Amount   float64
    Timestamp time.Time
}

// BankAccount simulates a bank account with transactions and reports the balance after each transaction
type BankAccount struct {
    Balance float64
    Transactions []Transaction
}

func (ba *BankAccount) Deposit(amount float64) {
    ba.Balance += amount
    ba.Transactions = append(ba.Transactions, Transaction{Type: "Deposited", Amount: amount, Timestamp: time.Now()})
}

func (ba *BankAccount) Withdraw(amount float64) {
    if amount > ba.Balance {
        panic("Insufficient funds")
    }
    ba.Balance -= amount
    ba.Transactions = append(ba.Transactions, Transaction{Type: "Withdrawn", Amount: amount, Timestamp: time.Now()})
}

func (ba *BankAccount) GetBalance() float64 {
    return ba.Balance
}

// ReportTransations prints the history of transactions on the account
func (ba *BankAccount) ReportTransactions() []Transaction {
    return ba.Transactions
}

func main() {
    // Initialize a new bank account with an initial balance
    account := &BankAccount{Balance: 1000.0}

    // Simulate some transactions over time
    rand.Seed(time.Now().UnixNano())
    for i := 0; i < 10; i++ {
        if rand.Intn(2) == 1 { // 50% chance of deposit or withdrawal
            var transactionType string
            switch rand.Intn(2) {
            case 0:
                transactionType = "Deposited"
            default:
                transactionType = "Withdrawn"
            }
            amount := float64(rand.Intn(200)) + 100 // Randomly choose between $100-$300 deposit or withdrawal
            account.Deposit(amount)
        } else {
            amount := float64(rand.Intn(200)) + 100
            account.Withdraw(amount)
        }

        fmt.Printf("Transaction %d: %s of $%.2f\n", i+1, transactionType, amount)
    }

    // Print the final balance and transaction history
    fmt.Println("\nFinal Balance:", account.GetBalance())
    for _, tx := range account.ReportTransactions() {
        fmt.Printf("%s of $%.2f at %v\n", tx.Type, tx.Amount, tx.Timestamp)
    }
}

//
//  ExpenseHistory.swift
//  expenseCalculator
//
//  Created by Pranav on 15/05/20.
//  Copyright © 2020 Pranav. All rights reserved.
//

import Foundation
import UIKit

import CoreData




class ExpenseHistoryViewController:   UIViewController, UITableViewDataSource {
    
    
//    @IBOutlet weak var historyTable: UITableView!
    
    var expenses: [ExpenseEntity] = []
    
     func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    
     func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        self.expenses.count
    }
    
     func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let cell = tableView.dequeueReusableCell(withIdentifier: "historyCellType",
        for: indexPath) as! HistoryTableCell

        
//        cell.textLabel?.text = self.expenses[indexPath.row].title
//        cell.detailTextLabel?.text = "spent on: \(self.expenses[indexPath.row].spentOn) cost: \(self.expenses[indexPath.row].cost)"
        
        cell.title.text = self.expenses[indexPath.row].title
        cell.spentOn.text = "\(self.expenses[indexPath.row].spentOn)"
        cell.cost.text = "Rs. \(self.expenses[indexPath.row].cost)"
        return cell
    }

    
//    func tableView(_ tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
//        self.shouldPerformSegue(withIdentifier: "edit_expense", sender: self)
//    }
    
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        
        if(segue.identifier == "edit_expense"){
            let upComing: AddExpenseViewController = segue.destination as! AddExpenseViewController
            
            upComing.isFromEditExpense = true
            
//            guard let row = self.historyTable?.indexPathForSelectedRow?.row else { return }
            
//            let expenseAtRow = self.expenses[row]
//
//            upComing.editExpenseCost = expenseAtRow.cost
//
//            upComing.editExpenseDate = expenseAtRow.spentOn
//
//            upComing.editExpenseTitle = expenseAtRow.title
            
        }
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let fetchRequest = NSFetchRequest<ExpenseEntity>(entityName: "ExpenseEntity")
        
        guard let appDelegate = UIApplication.shared.delegate as? AppDelegate else {return}
        
        let managedContext = appDelegate.persistentContainer.viewContext

        
        
        do {
            self.expenses = try managedContext.fetch(fetchRequest)

        } catch let error as NSError{
            print("Couldn't fetch there was this error: \(error)")
        }
//        DispatchQueue.main.async {
//                           self.historyTable.reloadData()
//                       }

        
    }
    
}

//
//  ExpenseHistoryTablViewController.swift
//  expenseCalculator
//
//  Created by Pranav on 16/05/20.
//  Copyright © 2020 Pranav. All rights reserved.
//

import Foundation

import UIKit

import CoreData

class ExpenseHistoryTableViewController: UIViewController, UITableViewDataSource, UITableViewDelegate, NSFetchedResultsControllerDelegate{
    
    var expenses: [ExpenseEntity] = []
    
    @IBOutlet weak var historyTableOutlet: UITableView!
    
    var fetchedResultsController: NSFetchedResultsController<ExpenseEntity>!
    
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print("Hey there you are selected \(indexPath)")
        self.performSegue(withIdentifier: "edit_expense", sender: self)
    }
    
    
    
    func numberOfSections(in tableView: UITableView) -> Int {
        if let sections = fetchedResultsController.sections {
            return sections.count
        }
        
        return 0
    }
    
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        if let sections = fetchedResultsController.sections {
            let currentSection = sections[section]
            return currentSection.numberOfObjects
        }
        
        return 0
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let cell = tableView.dequeueReusableCell(withIdentifier: "historyCellType",
                                                 for: indexPath) as! HistoryTableCell
        
        let expense = fetchedResultsController.object(at: indexPath)
        
        let formatter1 = DateFormatter()
        formatter1.dateStyle = .short
        let shortSpentOn = formatter1.string(from: expense.spentOn)
        cell.title.text = expense.title
        cell.spentOn.text = shortSpentOn
        cell.cost.text = "Rs. \(expense.cost)"
        return cell
    }
    
    
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        print("Ur inside prepare")
        if(segue.identifier == "edit_expense"){
            print("Inside edit_expense")
            let upComing: AddExpenseViewController = segue.destination as! AddExpenseViewController
            
            upComing.isFromEditExpense = true
            
            guard let row = self.historyTableOutlet?.indexPathForSelectedRow else { return }
            
            let expenseAtRow = fetchedResultsController.object(at: row)
            
            upComing.editExpenseCost = expenseAtRow.cost
            
            upComing.editExpenseDate = expenseAtRow.spentOn
            
            upComing.editExpenseTitle = expenseAtRow.title
            
        }
    }
    
    func configureFetchedResultsController() {
        
//        let fetchRequest = NSFetchRequest<ExpenseEntity>(entityName: "ExpenseEntity")
        guard let appDelegate = UIApplication.shared.delegate as? AppDelegate else {return}
        let managedContext = appDelegate.persistentContainer.viewContext


        let expenseFetchRequest = NSFetchRequest<ExpenseEntity>(entityName: "ExpenseEntity")
        let primarySortDescriptor = NSSortDescriptor(key: "spentOn", ascending: false)
//        let secondarySortDescriptor = NSSortDescriptor(key: "commonName", ascending: true)
        expenseFetchRequest.sortDescriptors = [primarySortDescriptor]
        
        self.fetchedResultsController = NSFetchedResultsController<ExpenseEntity>(
            fetchRequest: expenseFetchRequest,
            managedObjectContext: managedContext,
            sectionNameKeyPath: nil,
            cacheName: nil)
        
        self.fetchedResultsController.delegate = self
        
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        historyTableOutlet.dataSource = self
        historyTableOutlet.delegate = self
        
        
        
        configureFetchedResultsController()
        
        do {
            try fetchedResultsController.performFetch()
        } catch {
            print("An error occurred")
            
        }
//        do {
//            self.expenses = try managedContext.fetch(fetchRequest)
//
//        } catch let error as NSError{
//            print("Couldn't fetch there was this error: \(error)")
//        }
//        DispatchQueue.main.async {
//            self.historyTableOutlet.reloadData()
//        }
    }
    
    func controllerWillChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
        self.historyTableOutlet.beginUpdates()
    }
    
    func controllerDidChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
        self.historyTableOutlet.endUpdates()
    }
    
    func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange anObject: Any, at indexPath: IndexPath?, for type: NSFetchedResultsChangeType, newIndexPath: IndexPath?) {
        
        switch type{
        case .insert:
            if let indexPath = newIndexPath{
                self.historyTableOutlet.insertRows(at: [indexPath], with: UITableView.RowAnimation.fade)
            }
        case .delete:
            if let deleteIndexPath = indexPath{
                self.historyTableOutlet.deleteRows(at: [deleteIndexPath], with: UITableView.RowAnimation.fade)
            }
        case .update:
            if let updateIndexPath = indexPath{
                let cell = self.historyTableOutlet.cellForRow(at: updateIndexPath) as! HistoryTableCell
                let expense = self.fetchedResultsController.object(at: updateIndexPath) as ExpenseEntity
                
                let formatter1 = DateFormatter()
                formatter1.dateStyle = .short
                let shortSpentOn = formatter1.string(from: expense.spentOn)
                
                cell.title.text = expense.title
                cell.spentOn.text = shortSpentOn
                cell.cost.text = "Rs. \(expense.cost)"
                
            }
        case .move:
            if let deleteIndexPath = indexPath {
                self.historyTableOutlet.deleteRows(at: [deleteIndexPath], with: UITableView.RowAnimation.fade)
            }
            // Note that for Move, we insert a row at the __newIndexPath__
            if let insertIndexPath = newIndexPath {
                self.historyTableOutlet.insertRows(at: [insertIndexPath], with: UITableView.RowAnimation.fade)
            }
        @unknown default:
            fatalError("Unkown error occured")
        }
        
    }
}

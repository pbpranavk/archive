//
//  AddExpenseViewController.swift
//  expenseCalculator
//
//  Created by Pranav on 15/05/20.
//  Copyright © 2020 Pranav. All rights reserved.
//

import Foundation
import UIKit

import CoreData

class AddExpenseViewController: UIViewController{
    
    
    var userName:String?
    
    var isFromEditExpense:Bool?
    
    var editExpenseTitle: String?
    
    var editExpenseCost: Double?
    
    var editExpenseDate: Date?
    
    @IBOutlet weak var deleteExpense: UIButton!
    
    @IBOutlet weak var welcomeMsg: UILabel!
    
    @IBOutlet weak var expenseTitle: UITextField!
    
    @IBOutlet weak var expenseAmount: UITextField!
    
    @IBOutlet weak var isToday: UISwitch!
    
    
    
    @IBOutlet weak var olderDate: UIDatePicker!
    
    @IBOutlet weak var olderDateLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        welcomeMsg.text = "Hello there, \(userName ?? "PK")"
        
        deleteExpense.isHidden = true
        
        
        if self.isFromEditExpense ?? false{
            
            expenseTitle.text = editExpenseTitle
            
            expenseAmount.text = "\(editExpenseCost ?? 0.0)"
            
            print(editExpenseDate!)
            print(Date())
            
            let formatter1 = DateFormatter()
            formatter1.dateStyle = .short

            let shortEditExpenseDate = formatter1.string(from: editExpenseDate ?? Date())
            
            let today = formatter1.string(from: Date())
            
            if(shortEditExpenseDate == today){
                isToday.setOn(true, animated: true)
            }else{
                isToday.setOn(false, animated: false)
                olderDate.isHidden = false
                olderDateLabel.isHidden = false
                olderDate.date = editExpenseDate ?? Date()
            }
            
            deleteExpense.isHidden = false
            
        }
    }
    @IBAction func logout(_ sender: Any) {
        dismiss(animated: true, completion: nil)
    }
    
    @IBAction func isTodayToggled(_ sender: Any) {
        if isToday.isOn{
            olderDate.isHidden = true
            olderDateLabel.isHidden = true
        }else {
            olderDate.isHidden = false
            olderDateLabel.isHidden = false
        }
    }
    
    @IBAction func saveExpense(_ sender: Any) {
        guard let appDelegate = UIApplication.shared.delegate as? AppDelegate else {return}
        
        let managedContext = appDelegate.persistentContainer.viewContext
        
        
        if(isFromEditExpense ?? false){
            let fetchRequest = NSFetchRequest<ExpenseEntity>(entityName: "ExpenseEntity")
            fetchRequest.predicate = NSPredicate(format: "title = %@", editExpenseTitle!)
            do{
                let fetchResults = try managedContext.fetch(fetchRequest)
                
                if fetchResults.count > 0{
                    let managedObject : ExpenseEntity = fetchResults[0]
                    
                    let newcost :Double? = Double(expenseAmount.text!)
                    let newTite : String = expenseTitle.text ?? "Default Value"
                    managedObject.setValue(newcost, forKey: "cost")
                    managedObject.setValue(newTite, forKey: "title")
                    if isToday.isOn{
                        managedObject.setValue(Date(), forKey: "spentOn")
                    }else{
                        managedObject.setValue(olderDate.date, forKey: "spentOn")
                    }
                }
                
            }catch{
                print("Fatal error \(error)")
            }
        }else{
            let expense = NSEntityDescription.insertNewObject(forEntityName: "ExpenseEntity", into: managedContext) as! ExpenseEntity
            
            let cost :Double? = Double(expenseAmount.text!)
            
            expense.cost = cost ?? 0.0
            
            expense.title = expenseTitle.text ?? "Default Value"
            if isToday.isOn{
                expense.spentOn = Date()
            }else{
                expense.spentOn = olderDate.date
            }
        }
        
        do{
            try managedContext.save()
            print("Save successfull")
        } catch let error as NSError{
            print("Couldn't save \(error)")
        }
        
        
    }
    
    
}

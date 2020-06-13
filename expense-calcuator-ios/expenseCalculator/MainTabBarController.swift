//
//  MainTabBarController.swift
//  expenseCalculator
//
//  Created by Pranav on 15/05/20.
//  Copyright © 2020 Pranav. All rights reserved.
//

import Foundation
import UIKit

import CoreData

class MainTabBarController: UITabBarController{
    
    var userName: String?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        guard let viewControllers = viewControllers else {
            return
        }
        
        
        for viewController in viewControllers{
            if let addExpenseNavigationController = viewController as? AddExpenseNavigationController{
                if let addExpenseViewController = addExpenseNavigationController.viewControllers.first as? AddExpenseViewController {
                    addExpenseViewController.userName = userName
                }
            }
        }
    }
}

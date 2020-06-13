//
//  LoginViewController.swift
//  expenseCalculator
//
//  Created by Pranav on 15/05/20.
//  Copyright © 2020 Pranav. All rights reserved.
//

import Foundation

import UIKit
import CoreData

class LoginViewController: UIViewController {

    @IBOutlet weak var userNameTextField: UITextField!
    @IBOutlet weak var passwordTextField: UITextField!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func loginTapped(_ sender: Any) {
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if let mainTabBarController = segue.destination as? MainTabBarController{
            mainTabBarController.userName = userNameTextField.text
        }
    }


}


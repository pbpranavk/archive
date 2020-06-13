//
//  PersistentContainer.swift
//  expenseCalculator
//
//  Created by Pranav on 15/05/20.
//  Copyright © 2020 Pranav. All rights reserved.
//

//TODO: Is this file required??

import Foundation

import CoreData

class PersistentContainer: NSPersistentContainer {

    func saveContext(backgroundContext: NSManagedObjectContext? = nil) {
        let context = backgroundContext ?? viewContext
        guard context.hasChanges else { return }
        do {
            try context.save()
        } catch let error as NSError {
            print("Error: \(error), \(error.userInfo)")
        }
    }
}

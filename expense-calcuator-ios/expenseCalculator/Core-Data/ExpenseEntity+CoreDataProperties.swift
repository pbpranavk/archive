//
//  ExpenseEntity+CoreDataProperties.swift
//  expenseCalculator
//
//  Created by Pranav on 15/05/20.
//  Copyright © 2020 Pranav. All rights reserved.
//
//

import Foundation
import CoreData


extension ExpenseEntity {

    @nonobjc public class func fetchRequest() -> NSFetchRequest<ExpenseEntity> {
        return NSFetchRequest<ExpenseEntity>(entityName: "ExpenseEntity")
    }

    @NSManaged public var title: String
    @NSManaged public var cost: Double
    @NSManaged public var spentOn: Date

}

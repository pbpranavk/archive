//
//  ExploreMoya.swift
//  expenseCalculator
//
//  Created by Pranav on 19/05/20.
//  Copyright © 2020 Pranav. All rights reserved.
//

import Foundation

import UIKit

import Moya

class ExploreMoya: UIViewController{
    
    let provider = MoyaProvider<StarWars>()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        provider.request(<#T##target: StarWars##StarWars#>) { (result) in
            switch result{
            case .success(let response):
                debugPrint(response)
            case .failure(let error):
                debugPrint(error)
            }
        }
    }
}

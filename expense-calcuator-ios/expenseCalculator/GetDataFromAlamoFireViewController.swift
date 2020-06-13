//
//  GetDataFromAlamoFireViewController.swift
//  expenseCalculator
//
//  Created by Pranav on 18/05/20.
//  Copyright © 2020 Pranav. All rights reserved.
//

import Foundation

import UIKit

import Alamofire


class GetDataFromAlamoFireViewController: UIViewController{
    
    func fetchFilms(){
        let request = AF.request("http://swapi.dev/api/films")
            request.responseJSON{ (data) in
                print(data)
        }
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        
//        AF.request("https://httpbin.org/get").response{ response in
//            debugPrint(response)
//        }
        
        fetchFilms()
    }
}

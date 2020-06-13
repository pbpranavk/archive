//
//  StarWars.swift
//  expenseCalculator
//
//  Created by Pranav on 19/05/20.
//  Copyright © 2020 Pranav. All rights reserved.
//

import Foundation

import Moya

public enum StarWars{
    
    case films
}


extension StarWars: TargetType{
    public var baseURL: URL {
        return URL(string: "http://swapi.dev/api")!
    }
    
    public var path: String {
        switch self {
        case .films:
            return "/films"
        
        }
    }
    
    public var method: Moya.Method {
        switch self {
        case .films:
            return .get
        
        }
    }
    
    public var sampleData: Data {
        return Data()
    }
    
    public var task: Task {
        return .requestPlain
    }
    
    public var headers: [String : String]? {
        return ["Content-Type" : "application/json"]
    }
    
    public var validationType: ValidationType {
      return .successCodes
    }
    
}

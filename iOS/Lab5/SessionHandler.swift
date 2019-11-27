//
//  SessionHandler.swift
//  Lab5
//
//  Created by Will Lacey on 11/19/19.
//  Copyright © 2019 Will Lacey. All rights reserved.
//

let SERVER_URL = "http://10.8.103.99:8000"

import UIKit

class SessionHandler: NSObject, URLSessionDelegate {
    
    // MARK: Class Properties
    var session = URLSession()
    let operationQueue = OperationQueue()

    var ringBuffer = RingBuffer()
    
    var isWaitingForData = false
    
    override init() {
        super.init()
        
        let sessionConfig = URLSessionConfiguration.ephemeral
        
        sessionConfig.timeoutIntervalForRequest = 5.0
        sessionConfig.timeoutIntervalForResource = 8.0
        sessionConfig.httpMaximumConnectionsPerHost = 1
        
        self.session = URLSession(configuration: sessionConfig,
            delegate: self,
            delegateQueue:self.operationQueue)
    }
    
    func testPhoneConnection() {
        let baseURL = "\(SERVER_URL)/TestServerConnection"
        let getUrl = URL(string: baseURL)
        let request: URLRequest = URLRequest(url: getUrl!)
        let dataTask : URLSessionDataTask = self.session.dataTask(with: request,
            completionHandler:{(data, response, error) in
                if(error != nil){
                    print("Response:\n\t", response ?? "Could not connect to server.")
                }
                else{
                    let jsonDictionary = self.convertDataToDictionary(with: data)

                    if let bool = jsonDictionary["valid"]{
                        NSLog("\(bool): Valid Connection with Server")
                    } else {
                        NSLog("Invalid Connection with Server")
                    }
                }

        })

        dataTask.resume() // start the task
    }
    
    func setPlayers(whitePlayerID: Int, blackPlayerID: Int) {
        let baseURL = "\(SERVER_URL)/SetPlayers"
        let postUrl = URL(string: "\(baseURL)")
        
        // create a custom HTTP POST request
        var request = URLRequest(url: postUrl!)
        
        // data to send in body of post request (send arguments as json)
        let jsonUpload:NSDictionary = ["w_id":whitePlayerID,
                                       "b_id":blackPlayerID]
        
        
        let requestBody:Data? = self.convertDictionaryToData(with:jsonUpload)
        
        request.httpMethod = "POST"
        request.httpBody = requestBody
        
        let postTask : URLSessionDataTask = self.session.dataTask(with: request,
            completionHandler:{(data, response, error) in
                if(error != nil){
                    if let res = response{
                        print("Response:\n",res)
                    }
                }
                else{
                    let jsonDictionary = self.convertDataToDictionary(with: data)
                    NSLog("\(jsonDictionary["valid"]!): Valid Player upload")
                }

        })
        
        postTask.resume() // start the task
    }
    
    //MARK: JSON Conversion Functions
    func convertDictionaryToData(with jsonUpload:NSDictionary) -> Data?{
        do { // try to make JSON and deal with errors using do/catch block
            let requestBody = try JSONSerialization.data(withJSONObject: jsonUpload, options:JSONSerialization.WritingOptions.prettyPrinted)
            return requestBody
        } catch {
            print("json error: \(error.localizedDescription)")
            return nil
        }
    }
    
    func convertDataToDictionary(with data:Data?)->NSDictionary{
        do { // try to parse JSON and deal with errors using do/catch block
            let jsonDictionary: NSDictionary =
                try JSONSerialization.jsonObject(with: data!,
                                              options: JSONSerialization.ReadingOptions.mutableContainers) as! NSDictionary
            
            return jsonDictionary
            
        } catch {
            print("json error: \(error.localizedDescription)")
            return NSDictionary() // just return empty
        }
    }
    
}

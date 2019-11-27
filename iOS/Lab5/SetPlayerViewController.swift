//
//  SetPlayerViewController.swift
//  Lab5
//
//  Created by Will Lacey on 11/12/19.
//  Copyright © 2019 Will Lacey. All rights reserved.
//

import UIKit

class SetPlayerController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource {
    
    @IBOutlet weak var pickerWhite: UIPickerView!
    @IBOutlet weak var pickerBlack: UIPickerView!
    
    var pickerData: [String] = []
    
    let sessionHandler = SessionHandler.init()
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        let navBar = self.navigationController?.navigationBar
        navBar?.isHidden = true
        
        self.view.backgroundColor = UIColor(red: 36/256, green: 45/256, blue: 61/256, alpha: 1)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Connect data:
        self.pickerWhite.delegate = self
        self.pickerWhite.dataSource = self
        self.pickerBlack.delegate = self
        self.pickerBlack.dataSource = self
        
        self.pickerData = ["Human", "AI Random", "AI CNN1", "AI MLP1", "AI MLP2", "AI MLP3"]
    }

    override var prefersStatusBarHidden: Bool {
        return true
    }
    
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return self.pickerData.count
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        return self.pickerData[row]
    }
    
    func pickerView(_ pickerView: UIPickerView, attributedTitleForRow row: Int, forComponent component: Int) -> NSAttributedString? {

        return NSAttributedString(string: pickerData[row], attributes: [NSAttributedString.Key.foregroundColor: UIColor.white])
    }
    
    @IBAction func exitButtonPressed(_ sender: Any) {
        
        let wID = pickerWhite.selectedRow(inComponent: 0)
        let bID = pickerBlack.selectedRow(inComponent: 0)
        
        self.sessionHandler.setPlayers(whitePlayerID: wID, blackPlayerID: bID)
        
        self.navigationController?.popViewController(animated: true)
    }
    
}

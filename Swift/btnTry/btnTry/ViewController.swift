//
//  ViewController.swift
//  btnTry
//
//  Created by Student on 01/09/23.
//  Copyright © 2023 lpu. All rights reserved.
//

import UIKit
import QuartzCore

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        btn.backgroundColor = UIColor.blue
        btn.tintColor = UIColor.white
        txtOut.alpha = 0.5
        txtOut.layer.cornerRadius = 20.0
        btn.layer.cornerRadius = 20.0
        lbl1.backgroundColor = UIColor.orange
        lbl1.layer.cornerRadius = 5
        lbl1.layer.masksToBounds = true
        lbl1.alpha = 0.3
        view.backgroundColor = UIColor.gray
        lbl2.textColor = UIColor.red
    }
    
    @IBOutlet var out1: UISwitch!
    
    @IBAction func act1(_ sender: Any) {
        if(out1.isOn) {
            lbl1.text = "switch is on"
            btn.isEnabled = true
            btn.isHidden = false
            txtOut.isEnabled = true
            view.backgroundColor = UIColor.gray
        }
        else {
            lbl1.text = "switch is off"
            btn.isEnabled = false
            btn.isHidden = true
            txtOut.isEnabled = false
            view.backgroundColor = UIColor.brown
        }
    }
    
    @IBOutlet var lbl1: UILabel!
    @IBOutlet var seg1: UISegmentedControl!
    @IBOutlet var lbl2: UILabel!
    @IBOutlet var btn: UIButton!
    @IBOutlet var txtOut: UITextField!
    @IBAction func segFunc(_ sender: Any) {
        if(seg1.selectedSegmentIndex == 0) {
            lbl2.text = "Let's Chat"
            view.backgroundColor = UIColor(red: 0.3, green: 0.2, blue: 0.2, alpha: 1.00)
        }
        else if(seg1.selectedSegmentIndex == 1) {
            lbl2.text = "Welcome to status"
            view.backgroundColor = UIColor(red: 0.2, green: 0.3, blue: 0.2, alpha: 1.00)
        }
        else {
            lbl2.text = "Welcome to Contacts"
            view.backgroundColor = UIColor(red: 0.3, green: 0.2, blue: 0.3, alpha: 1.00)
        }
    }
    
    @IBOutlet var sliderOut: UISlider!
    @IBAction func sliderAct(_ sender: Any) {
        lbl2.text = String(sliderOut.value)
    }
    
}


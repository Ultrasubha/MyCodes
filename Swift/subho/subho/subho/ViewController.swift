//
//  ViewController.swift
//  subho
//
//  Created by Student on 18/08/23.
//  Copyright © 2023 Student. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        initialSetup()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    public func initialSetup() {
        view.backgroundColor = .gray
        navigationItem.title = "something"
    }

  
    @IBOutlet weak var v1: UILabel!
    
    
    @IBOutlet var var1: UIView!
    
    
    @IBOutlet weak var txt1: UITextField!
    @IBOutlet weak var clickLabel: UIButton!
    
    var num = 0
    @IBAction func call(_ sender: Any) {
        self.v1.textColor = UIColor.red
        self.v1.backgroundColor = UIColor.green
        var s = "Wah"
        print(s, s.count)
        self.v1.layer.cornerRadius = 70
        self.clickLabel.backgroundColor = UIColor.brown
        var x1 : Int? = Int(txt1.text!)
        
        x1! += 1
        s += String(x1!)
        s += (x1! % 2 == 0 ) ? " even num " : " odd num "
        num += 1
        s += String(num)
        self.v1.text = s
        //print(clickLabel.)
        //self.clickLabel.clibackgroundColor = UIColor.yellow
    }
}


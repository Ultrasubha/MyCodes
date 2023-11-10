//
//  ResultViewController.swift
//  SubhadeepCa3
//
//  Created by Student on 08/11/23.
//  Copyright © 2023 lpu. All rights reserved.
//

import UIKit

class ResultViewController: UIViewController, UITextFieldDelegate {

    
    @IBOutlet weak var tasktxt: UITextField!
    @IBOutlet weak var datetxt: UITextField!
    @IBOutlet weak var timetxt: UITextField!
    @IBOutlet weak var venuetxt: UITextField!
    
    @IBOutlet weak var btn: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.btn.layer.cornerRadius = 5
        self.btn.layer.borderWidth = 1
        self.tasktxt.delegate = self
        self.datetxt.delegate = self
        self.timetxt.delegate = self
        self.venuetxt.delegate = self
    }
    
    @IBAction func confirm(_ sender: Any) {
        var alert = UIAlertController(title: "Task", message: "Saved Successfully", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "Ok", style: .default) {
            Void in
            self.performSegue(withIdentifier: "pichhe", sender: self)

        })
        self.present(alert, animated: true, completion: nil)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        var s = String()
        s = datetxt.text! +  " | " + timetxt.text! + " | " + tasktxt.text!
        let vc = segue.destination as! ViewController
        vc.data.append(s)
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        self.view.endEditing(true)
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        tasktxt.resignFirstResponder()
        datetxt.resignFirstResponder()
        timetxt.resignFirstResponder()
        venuetxt.resignFirstResponder()
        return true
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}

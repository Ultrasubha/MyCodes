//
//  AddEntryViewController.swift
//  subh
//
//  Created by Student on 03/11/23.
//  Copyright © 2023 lpu. All rights reserved.
//

import UIKit

protocol AddEntryDelegate: AnyObject {
    func addTimetableEntry(_ timetableEntry: Timetable)
}

class AddEntryViewController: UIViewController {
    @IBOutlet weak var dayTextField: UITextField!
    @IBOutlet weak var timeTextField: UITextField!
    @IBOutlet weak var subjectTextField: UITextField!
    
    weak var delegate: AddEntryDelegate?
    
    @IBAction func saveButtonTapped(_ sender: UIButton) {
        guard let day = dayTextField.text, let time = timeTextField.text, let subject = subjectTextField.text else {
            return
        }
        
        let timetableEntry = Timetable(day: day, time: time, subject: subject)
        delegate?.addTimetableEntry(timetableEntry)
        navigationController?.popViewController(animated: true)
    }
}

    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */



//
//  ViewController.swift
//  subh
//
//  Created by Student on 03/11/23.
//  Copyright © 2023 lpu. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var tableView: UITableView!
    
    var timetableData: [Timetable] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.delegate = self
        tableView.dataSource = self
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "AddEntrySegue" {
            if let addEntryVC = segue.destination as? AddEntryViewController {
                addEntryVC.delegate = self
            }
        }
    }
    @IBAction func addEntryButtonTapped(_ sender: Any) {
        performSegue(withIdentifier: "AddEntrySegue", sender: self)
    }
    
}

extension ViewController: UITableViewDataSource, UITableViewDelegate {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return timetableData.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "TimetableCell", for: indexPath)
        let timetableEntry = timetableData[indexPath.row]
        
        cell.textLabel?.text = timetableEntry.day
        cell.detailTextLabel?.text = "\(timetableEntry.time) - \(timetableEntry.subject)"
        
        return cell
    }
}

extension ViewController: AddEntryDelegate {
    func addTimetableEntry(_ timetableEntry: Timetable) {
        timetableData.append(timetableEntry)
        tableView.reloadData()
    }
}


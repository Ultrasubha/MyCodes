//
//  ViewController.swift
//  SubhadeepCa3
//
//  Created by Student on 08/11/23.
//  Copyright © 2023 lpu. All rights reserved.
//

import UIKit

class ViewController: UITableViewController {
    
    var data = ["08-11-2023 | 02:00 PM | Create IOS Project" ,
                "10-11-2023 | 08:00 AM | IOS Project Submit" ,
                "11-11-2023 | 07:00 PM | codechef contest 12",
                "13-11-2023 | 08:00 PM | codeforces contest 45",
                "15-11-2023 | 10:00 AM | Machine Learning CA",
                "18-11-2023 | 07:00 PM | codechef contest 12",
                "20-11-2023 | 00:00 PM | Computer Vision CA",
                "21-11-2023 | 00:00 PM | Leetcode contest 18",
                ]

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 50
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print(self.data[indexPath.row])
    }
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return self.data.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "LabelCell", for: indexPath)
        cell.textLabel?.text = self.data[indexPath.row]
        return cell
    }
    @IBAction func addTask(_ sender: Any) {
        performSegue(withIdentifier: "samne", sender: self)
    }
    
    
}


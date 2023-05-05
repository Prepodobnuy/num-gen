use std::fs::File;
use std::io::Read;
use std::io::Write;

fn fillspace(num : String) -> String {
    let len = num.len();
    if len != 7 {
        return "0".repeat(7-len)
    }
    return "".to_string()   
}

fn isitcontains(num : String) -> bool {
    if num.contains("0000") || num.contains("1111") || num.contains("2222") || num.contains("3333") || num.contains("4444") || num.contains("5555") || num.contains("6666") || num.contains("7777") || num.contains("8888") || num.contains("9999") {
        return false
    } 
    return true
}

fn main() {
    let mut f : File = File::open("ccode.cfg").expect("Error opening file");
    let mut numcode = String::new();
    f.read_to_string(&mut numcode).expect("Error reading file");
    
    let mut f : File = File::open("code.cfg").expect("Error opening file");
    let mut opecode = String::new();
    f.read_to_string(&mut opecode).expect("Error reading file");

    let mut f : File = File::open("path.cfg").expect("Error opening file");
    let mut filepath = String::new();
    f.read_to_string(&mut filepath).expect("Error reading file");

    let mut i: u128 = 0;

    let mut f = File::create(filepath).expect("Error creating file");

    while i != 10000000 {

        if isitcontains(i.to_string()) {
            let ncode = numcode.to_string();
            let res = ncode + &opecode + &fillspace(i.to_string()) + &i.to_string() + &"\n";
            f.write_all(res.as_bytes()).expect("Error writing to file");
        }
        i += 1;
    }
}
use std::fmt::Debug;

struct Rect{
    height:u32,
    width:u32,
}

#[derive(Copy,Clone)]
enum Direction{
 North,
 East,
 West,
 South,
}

impl Rect{
    pub fn area(&self)->u32{
        return self.height*self.width;
    }
    pub fn perimeter(&self)->u32{
        return 2*(self.height + self.width);
    }
}

fn main() {
    println!("Hello, world!");
    let is_male:bool = true;
    let is_above_18:bool = true;

    if is_male{
        println!("You are a male")
    }
    else{
        println!("You are not a male")
    }

    if is_male && is_above_18{
        println!("You are male and of legal age ")
    }

    let greeting:String=String::from("Hello World !");

    println!("{}",greeting);

    let char1:Option<char>=greeting.chars().nth(0);

    println!("char1:{}", char1.unwrap());

    let is_even:bool = true;

    if is_even{
        println!("This is even number");
    }else if !is_even{
        println!("This is odd number");
    }
    
    for i in 0..11{
        print!("{} ", i);
    }
    
    let sentence:String = String::from("Hello , this is from Adarsh");
    let first_word:String = get_first_word(sentence);

    println!("First word of the sentence : {}",first_word);

    let a:i32 = 10;
    let b:i32=20;

    let result = do_sum(a,b);

    println!("Sum of {} and {} is {} ", a, b, result);

    stack_fn(23,98);

    heap_fn();

    update_string();

    ownership_rule_1();
    ownership_rule_2();
    ownership_rule_3();
    ownership_rule_4();
    borrowing_rule_1();
    borrowing_rule_2();
    borrowing_rule_3();

    let rect:Rect = Rect {
        height:32,
        width:64,
    };

    println!("The area of the rectangle:{}", rect.area());
    println!("The perimeter of the rectangle:{}", rect.perimeter());

    let my_direction:Direction = Direction::North;
    move_direction(my_direction);

} 


fn move_direction(direction:Direction){
   match direction{
    Direction::East => println!("We are moving East"),
    Direction::North=> println!("We are moving North"),
    Direction::South=> println!("We are moving South"),
    Direction::West=> println!("We are moving West")
   }
}


pub fn get_first_word(sentence:String)->String{
    let mut ans:String = String::from("");
    for char in sentence.chars() {
        ans.push_str(char.to_string().as_str());
        if char == ' '{
           break;
        }
    }
    return ans;
}

pub fn do_sum(a:i32 , b:i32)->i32{
    return a+b;
}

pub fn stack_fn(a:i32 , b:i32){
  let c = a+b;
  println!("Stack function : Sum of {} and {} is {}", a, b,c);
}

pub fn heap_fn(){

    let s1:String=String::from("Hello");
    let s2:String=String::from("Adarsh");
    let combined = format!("{} {}",s1 ,s2);
    println!("Heap Function : The combined string is {} and {} is {}", s1, s2 , combined);
}

pub fn update_string(){
    let mut s:String = String::from("Hello");
    println!("Before we are updatig the string: {} ",s);
    println!("Capicity:{} , Length:{} , Pointer:{:p}", s.capacity(), s.len(), s.as_ptr());

    
    s.push_str("Add some additional text");
    println!("After we are updating the string: {}",s);
    println!("Capicity:{} , Length:{} , Pointer:{:p}", s.capacity(), s.len(), s.as_ptr());
}

pub fn ownership_rule_1(){

    let s1:String = String::from("Ownership Rule 1");
    println!("s1:{}", s1);
    println!("As soon as we start giving ownership of the variable to another variable , ownership change that variable which dont have ownershp dies");
    let s2 = s1;
    println!("s2:{}", s2);
}

pub fn ownership_rule_2(){
    let s1:String = String::from("Owenership Rule 2");
    println!("s1:{}",s1);
    let s2:String = s1.clone();
    println!("s1:{} : Now since we using cloned copy, it will not throw an error",s1);
    println!("Clone just create another copy of the variable of our variable , so variale is not out of ownership hence we dont get any error");
    println!("s2:{} :",s2);
}

pub fn ownership_rule_3(){
    let my_string:String = String::from("Owenership_Rule_3");
    take_ownership_rule_1(my_string);
    println!("when the string is passed in other function, it changed its ownership");
    println!("now if we call my string varible after passing it in a function it will give us an error")
}

pub fn take_ownership_rule_1(some_string:String){
    println!("Some string input is print here:{}", some_string)
}
pub fn ownership_rule_4(){
    let mut my_string=String::from("Ownership_Rule_4");
    my_string = take_ownership_rule_2(my_string);
    println!("String ownership : {}" , my_string);
    println!("Even through we are passing a string in the function, but since the string is mutable , hence it value can be changed , since we dont violated previous ownership rules and it still works, this is like we are giving ownership to someone else then taking back the ownership ")
}

pub fn take_ownership_rule_2(some_string:String)->String{
    println!("my_string {}", some_string);
    return some_string;
}

pub fn borrowing_rule_1(){
    let s1: String = String::from("Borrowing_Rule_1");
    println!("s1:{}", s1);
    let s2: &String = &s1;
    println!("s1:{} : Here s1 will still print without throwing an error since we are passing it value as reference means s2->s1-> value",s1);
    println!("s2:{}",s2);
}

pub fn borrowing_rule_2(){
    let my_string:String = String::from("Borrowing_Rule_2");
    println!("s1:{}",my_string);
    borrow_variable(&my_string);
}

pub fn borrow_variable(some_string:&String){
    println!("some string {}", some_string);
}


pub fn borrowing_rule_3(){
    let mut s1: String = String::from("Borrowing_Rule_3");
    let s2 : &mut String = &mut s1;
    s2.push_str(": Rule successfully understood");
    println!("{}",s1);
    println!("If our variable has one mutable reference, then the caraible cannot have anymore mutable and immutable references")
}
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
  println!("Sum of {} and {} is {}", a, b,c);
}

pub fn heap_fn(s1:String , s2:String){
    let combined = format!("{} {}",s1 ,s2);
    println!("The combined string is {} and {} is {}", s1, s2 , combined);
}
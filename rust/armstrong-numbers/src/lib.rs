pub fn is_armstrong_number(num: u64) -> bool {
    let number_str = num.to_string();
    let mut digits: Vec<u64> = Vec::new();

    for digit_char in number_str.chars() {
        if let Some(digit) = digit_char.to_digit(10) {
            digits.push(digit as u64);
        }
    }

    let num_digits = digits.len() as u32;
    let sum: u64 = digits.iter().map(|d| d.pow(num_digits)).sum();
    if sum == num {
        return true;
    }
    false
}

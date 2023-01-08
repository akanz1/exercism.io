// This stub file contains items that aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

pub fn production_rate_per_hour(speed: u8) -> f64 {
    if speed == 0 {
        return 0.0;
    }
    let mut success_rate = 100.0;

    if speed > 4 && speed <= 8 {
        success_rate = 90.0;
    } else if speed > 8 && speed <= 10 {
        success_rate = 77.0;
    };

    221.0 * speed as f64 / 100.0 * success_rate
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    production_rate_per_hour(speed) as u32 / 60
}

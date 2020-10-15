fn main() {
    struct User {
        user: String,
        id: u32,
    }
    let user = String::from("qwe");
    let mut user1 = User{
        user,
        id: 2,
    };
    let user2 = User{
        user: String::from("uhb"),
        ..user1
    };
    let user3 = User{
        id: 3,
        ..user1
    };
    // let user4 = User{
    //     id:4,
    //     ..user1
    // };
    user1.id = 223;
    println!("{}", user1.id);
    println!("{}", user2.id);
    println!("{}", user3.user)
}

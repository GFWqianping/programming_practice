
fn main() {
    enum MyEnum {
        MNone,
        Integer(i32),
    }
    let five = MyEnum::Integer(5);
    let four = MyEnum::Integer(4);
    match x {
        MNone => MNone,
        Integer(n) => Integer(n+1)
    }
}
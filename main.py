from functions import main, info, help, byebye
from switch import switch as sw

if __name__ == "__main__":
    print(main())
    while True:
        print("\n")
        rq = input("request: ")
        match rq:
            case "1": print(main())
            case "2": 
                sw()
                print(main())
            case "8": print(info())
            case "9": print(help())
            case "0": 
                print(byebye())
                break
        print("\n")

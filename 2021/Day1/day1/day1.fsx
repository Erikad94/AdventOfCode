open System.IO

let input = File.ReadAllLines("Day1/day1/input.txt") |> Array.map(fun x -> int x) |> Array.toList

let rec star1 (x:List<int>) =
    match x with
    //edge case, not gona happen but f# complains
    | [] -> 0
    //When there is only 1 element
    | lonely when (x.Length = 1) -> 0
    //Take first element and the rest of the list
    | current :: restList -> 
        //if current is smaller then next add 1
        if current < restList.Head then 
            1 + (star1 restList)
        else 
            star1 restList

let rec get3Values(y:List<int>) =
        match y with 
        //edge case, not gona happen but f# complains
        | [] -> []
        //when there is only 3 elements left
        | theEnd when (y.Length = 3) -> 
            [(theEnd |> List.sum)]
        //Take first element and the rest of the list
        | current :: restList -> 
            //add the next 2 add to current
            let values = current + (restList |> List.take (2) |> List.sum)
            //rebuild new list with only the sum of the 3 values and rec
            [ values ] @ get3Values(restList)

let rec star2 (x:List<int>) =
    star1(get3Values(x))
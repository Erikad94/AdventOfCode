open System.IO

let input = File.ReadAllLines("Day2/input.txt") |> Array.map(fun x -> x.Split(" ")) |> Array.toList

let rec star1 (x:string [] list, struct(a, b) ) =
    match x with
    //when there are no more directions
    | [] -> a*b
    //Take first element and the rest of the list
    | current :: restList -> 
        if current.[0] = "forward" then 
            star1 (restList,(a + int current.[1], b))
        elif current.[0] = "down" then 
            star1 (restList,(a, b + int current.[1]))
        else
            star1 (restList,(a, b - int current.[1]))

let rec star2 (x:string [] list, struct(a, b, c) ) =
    match x with
    //when there are no more directions
    | [] -> a*b
    //Take first element and the rest of the list
    | current :: restList -> 
        //It increases your horizontal position by X units.
        //increases your depth by your aim multiplied by X.
        if current.[0] = "forward" then 
            star2 (restList,(a + int current.[1], b + (c*int current.[1]), c))
        //increases your aim by X units.
        elif current.[0] = "down" then 
            star2 (restList,(a, b, c + int current.[1]))
        //decreases your aim by X units.
        else
            star2 (restList,(a, b, c - int current.[1]))

let rec start1(x:string [] list) =
    star1 (x, (0,0))

let rec start2(x:string [] list) =
    star2 (x, (0,0,0))
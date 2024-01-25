//
//  File.swift
//  codingTest
//
//  Created by 한수빈 on 1/24/24.
//

import Foundation

let n = Int(readLine()!)!
var arr : [Int] = []
for _ in 0..<n { arr.append(0) }
var input = readLine()!.split(separator: " ").map { Int(String($0))! }
var cnt = 0
while input != arr {
    for (index, num) in input.enumerated() {
        if num % 2 == 0 && index == input.endIndex - 1 {
            for (i, value) in input.enumerated() {
                input[i] = value/2
            }
            cnt += 1
            print(input)
            break
        }
        if num % 2 == 0 { continue }
        if input.max()! == num || (index == input.endIndex - 1) || input.min()! == num {
            input[index] = num - 1
            cnt += 1
        }
        print(input)
    }
    // 모든 요소가 짝수면, 나눈다.
    // 특정 요소가 홀수면 뺀다.
    // 특정 요소가 0이면 나누기만 한다.
    // 첫번째 예시가 안된다..조건을 하나둘 추가하다보니 어떻게 고쳐야할지 모르겠음
}
print(cnt)

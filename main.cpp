//
//  main.cpp
//  MyFirstProj
//
//  Created by Andres Columna on 9/12/18.
//  Copyright © 2018 Andres Columna. All rights reserved.
//

#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <unordered_set>
#include <ctime>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <chrono>
#include <math.h>

using namespace std;


int f(){
    return 10;
}

int main(int argc, const char * argv[]) {
    
    
    std::unordered_multiset<int> uset;
    std::multiset<int> set;

    ofstream setFile("set.txt");
    ofstream usetFile("uset.txt");
    
    
    // set precision
    setFile << fixed << showpoint;
    setFile << setprecision(8);
    cout << fixed << showpoint;
    cout << setprecision(8);
    usetFile << fixed << showpoint;
    usetFile << setprecision(8);
    
    //myfile << "Writing this to a file.\n";
    auto start = chrono::steady_clock::now();
    auto end = chrono::steady_clock::now();
    
    double elapsedTime = double(chrono::duration_cast<chrono::nanoseconds>(end-start).count());
    
    long long i = 1;
    int x = 0;
    
    int exponent = 23;

    while (i <= exponent){
        
        set.clear();
        uset.clear();
        
        double setRunTime = 0;
        double usetRunTime = 0;
        
        for(long long j = 0; j < pow(2, i); j++){
            
            x = rand();
            
            start = chrono::steady_clock::now();
            set.insert(x);
            end = chrono::steady_clock::now();
            setRunTime += double(chrono::duration_cast<chrono::nanoseconds>(end-start).count());
            
            start = chrono::steady_clock::now();
            uset.insert(x);
            end = chrono::steady_clock::now();
            usetRunTime += double(chrono::duration_cast<chrono::nanoseconds>(end-start).count());
        }
        
        setFile << setRunTime << "\n";
        usetFile << usetRunTime << "\n";
        
        i += 1;
    }
    
    

    setFile.close();
    usetFile.close();
    
    cout << "Success!\n";
    
    return 0;
}

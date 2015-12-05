#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
 
using namespace std;
 
void welcome();
void user_input(int& w, int& h, int& d);
void populate(int** maze, int& w, int& h, int& d)
bool mouse(int** maze);
int main(){
    //variable
    int width, height, density;
	srand(time());
    //input
    user_input(width, height, density);
    //create array
    int** maze[width+2][height+2];
    //populate
    populate(maze, width, height, densty);
     
     
     
}
 
void welcome();
 
void user_input(int& w, int& h, int& d){
    //input width
    cout << "Enter the width of the maze (1-99): ";
    cin >> w;
    cout << '\n';
    //input height
    cout << "Enter the height of the maze (1-99): ";
    cin >> h;
    cout << '\n';
    //input density
    cout << "Enter the density of the maze (1-99): ";
    cin >> d;
    cout << '\n';
}
 
void populate(int** maze, int& w, int& h, int& d){
	//int genwall;
	//generate wall
	for(int i = 0, i < h + 2, i++){
		maze[0][i] = 1;
		maze[w + 2][i] = 1
	}
	for(int i = 0, i < w + 2, i++){
		maze[i][0] = 1;
		maze[i][h + 2] = 1;
	}
	//use density for randomized walls
	for(int i = 1, i < w + 1, i++){
		for(int j = 1, j < h + 1, j++){
			//genwall = rand()%100;
			if(rand()%100 < d)
				maze[i][j] = 1;
			else 
				maze[i][j] = 0;
		}
	}
	maze[0][(rand() % h + 1)] = 0;
	maze[w + 2][(rand() % h + 1)] = 0;
}

bool mouse(int** maze){
	//place mouse at start
	do
	while()
}
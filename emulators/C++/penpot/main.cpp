#include <iostream>
#include <string>
#include <vector>

char loop(std::vector<std::string>& str, int x, int y){
	if(x < 0) x = str[0].size() - 1;
	if(y < 0) y = str.size() - 1;
	if(x == (signed)str[0].size()) x = 0; // etc etc mingw
	if(y == (signed)str.size()) y = 0;

	return str[y][x]; // too lazy to invert it in the drawing part, so I will invert it here
}

bool hasAAround(std::vector<std::string>& cells, int x, int y){
	bool exists = false;
	for(int i = -1; i <= 1; ++i){
		for(int j = -1; j <= 1; ++j){
			if(!(i == 0 && j == 0) && loop(cells, x+i, y+j) == 'A'){
				exists = true;
				break;
			}
		}
	}
	return exists;
}

int main(){
	int height;
	std::vector<std::string> inputCells;
	std::cout<<"Input the height: ";
	std::cin>>height;
	inputCells.resize(height);
	for(int i = 0; i < height; ++i){
		std::cout<<"Type the initial setup (line "<<i<<"): ";
		std::cin>>inputCells[i];
	}

	std::vector<std::string> cells = inputCells;
	// if want to see more steps just change this 10 to something else
	for(int re = 0; re < 10; ++re){
		std::vector<std::string> last_cells = cells;
		for(int i = 0; i < (signed)cells.size(); ++i){
			for(int j = 0; j < (signed)cells[0].size(); ++j){
				if(cells[i][j] == 'A'){
					cells[i][j] = 'B';
				}else if(cells[i][j] == 'B'){
					if(hasAAround(last_cells, j, i)){
						cells[i][j] = '0';
					}else{
						cells[i][j] = 'A';
					}
				}else if(cells[i][j] == '0'){
					if(hasAAround(last_cells, j, i)){
						cells[i][j] = 'A';
					}
				}
			}
		}
		for(auto& j : cells){
			std::cout<<j<<std::endl;
		}
		std::cout<<std::endl;
	}

	std::string pause;
	std::cin>>pause;
	return 0;
}

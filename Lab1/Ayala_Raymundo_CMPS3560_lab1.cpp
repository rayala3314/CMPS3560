#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdlib>
#include <bits/stdc++.h>

/*
*	Function that reads data from a CSV into a 2-D array.
*/
template <size_t rows, size_t cols>
void readCSV(double(&array)[rows][cols], char* filename) {
	std::ifstream file(filename);

	for (size_t row = 0; row < rows; ++row)
	{
		std::string line;
		std::getline(file, line);

		if (!file.good())
			break;

		std::stringstream iss(line);

		for (size_t col = 0; col < cols; ++col)
		{
			std::string val;
			std::getline(iss, val, ',');

			std::stringstream convertor(val);
			convertor >> array[row][col];
		}
	}
}

/*
*	Function that displays data valuesd
*/
template <size_t rows, size_t cols>
void displayValues(double(&array)[rows][cols]) {
	for (int row = 0; row < rows; ++row)
	{
		for (int col = 0; col < cols; col++) {
			std::cout << array[row][col] << ' ';
		}

		std::cout << std::endl;
	}
}


int main(int argc, char* argv[])
{
	// Your code here
	//Variables that are needed
	double petalLength;
	double flowerArray[100][2];
	double predictedArray[100][2];
	int irisVirginica = 2;
	int irisVersicolour = 1;
	double minPetal, maxPetal, stepSize, stepLength, thresholdVal, tempCorrect;
	double correct, newCorrect;
	correct = newCorrect = 0;
	char* flowerFile;
	
	//Max and min variables for petal length
	maxPetal = 0;
	minPetal = INT_MAX;

	//Get file from command line
	if (argc < 2) {
		std::cout << "Usage: ./lab1 [filename] float[step size]\n";
		exit(0);
	}
	flowerFile = argv[1];

	//Assign step size if not provided
	if (argc == 3)
		stepSize = atof(argv[2]);
	else 
		stepSize = 0.1;

	// Use readCSV to create data array
	readCSV(flowerArray, flowerFile);

	// displayValues
	displayValues(flowerArray);

	// for loop which classifies each element in array using if statement
	for (int row = 0; row < 100; ++row)
	{
		predictedArray[row][0] = flowerArray[row][0];
		petalLength = flowerArray[row][0];
		if (petalLength > 1.45) 
			predictedArray[row][1] = irisVirginica;
		
		else 
			predictedArray[row][1] = irisVersicolour;
	}
	// compare predicted class with groundtruth.
	for (int row = 0; row < 100; ++row)
	{
		if (flowerArray[row][1] == predictedArray[row][1])
			correct++;	
	}
	std::cout << "---------------" << std::endl;
	std::cout << "Percent correct: " << (correct / 100) * 100 << "%\n";


	/*-----  Part 2 ------ */

	std::cout << "Step Size Provided: " << stepSize << std::endl;

	for (int row = 0; row < 100; ++row)
	{
		//Find min and max lenghts of petals
		if (flowerArray[row][0] > maxPetal)
			maxPetal = flowerArray[row][0];
		if (flowerArray[row][0] < minPetal)
			minPetal = flowerArray[row][0];
	}

	//std::cout << "Max Petal Length: " << maxPetal << std::endl;
	//std::cout << "Min Petal Length: " << minPetal << std::endl;

	stepLength = minPetal;
	do
	{
		tempCorrect = 0;

		//Compare with different threshold values
		//Calculate correct Samples along the way
		for (int row = 0; row < 100; ++row)
		{
			petalLength = flowerArray[row][0];
			if (petalLength > stepLength)
				predictedArray[row][1] = irisVirginica;
			
			else
				predictedArray[row][1] = irisVersicolour;
			
	
			if(flowerArray[row][1] == predictedArray[row][1])
				tempCorrect++;

			if (tempCorrect > newCorrect) 
			{
				thresholdVal = stepLength;
				newCorrect = tempCorrect;
			}
		}

		stepLength += stepSize;

	} while (stepLength <= maxPetal);
	
	std::cout << "Improved percentage: " << (newCorrect / 100) * 100 << "%\n";
	std::cout << "At threshold value of: " << thresholdVal << std::endl;

	return 0;
}





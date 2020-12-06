# python-filters
## Usages
### TimeAveragingFilter
- Created by `TimeAveragingFilter(a_Weights=[0.5, 0.4, 0.2], a_Data=[], b_ValidateInputs=True)`
- Where:
 - a_Weights is an array containing weight values for each respective preceeding data point
 - a_Data is an *optional* array containing raw data which can have time averaging filters applied retroactively
 - b_ValidateInputs is an *optional* boolean value which verfies a_Weights and a_Data before applying filters
 
It is recommended that b_ValidateInputs is not set to False. Any errors that your input data may contain will be caught by the python interpreter and the errors raised will not be as diagnostic as the ones provided by the function which `b_ValidateInputs=True` pertains to

If a_Data is provided and created via `o_Filter = TimeAveragingFilter(a_Data)`, you can call either 
`o_Filter.FrontPropogateFilter()` 
or 
`o_Filter.BackPropogateFilter()`

Otherwise, the class should be created as follows:
1. Create an object
`o_Filter = TimeAveragingFilter(a_Weights=[0.7, 0.15, 0.10, 0.05])`
2. When new input is available, append it to `o_Filter.a_Data` using the `.Process(i_Data)` method
`o_Filter.Process(i_Data)`
This creates the data and appends it to the built-in data array, accessible by
`o_Filter.a_Data`

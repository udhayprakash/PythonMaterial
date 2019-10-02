import warnings

# warnings.simplefilter('error', UserWarning)
# It means to throw exceptionwhen error warning is present, 
print('BEFORE warning')
warnings.warn('This is not good practice')
print('AFTER warning')

# warnings.filterwarnings('ignore', category=DeprecationWarning)
# warnings.formatwarning()
# print(dir(warnings))
# help(warnings)

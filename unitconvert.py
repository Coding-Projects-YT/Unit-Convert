class UnitConverter:
    # Conversion factors to base units
    LENGTH_FACTORS = {
        'meter': 1.0,
        'meters': 1.0,
        'm': 1.0,
        'kilometer': 1000.0,
        'kilometers': 1000.0,
        'km': 1000.0,
        'centimeter': 0.01,
        'centimeters': 0.01,
        'cm': 0.01,
        'millimeter': 0.001,
        'millimeters': 0.001,
        'mm': 0.001,
        'mile': 1609.344,
        'miles': 1609.344,
        'yard': 0.9144,
        'yards': 0.9144,
        'foot': 0.3048,
        'feet': 0.3048,
        'inch': 0.0254,
        'inches': 0.0254,
    }

    MASS_FACTORS = {
        'kilogram': 1.0,
        'kilograms': 1.0,
        'kg': 1.0,
        'gram': 0.001,
        'grams': 0.001,
        'g': 0.001,
        'milligram': 0.000001,
        'milligrams': 0.000001,
        'mg': 0.000001,
        'pound': 0.45359237,
        'pounds': 0.45359237,
        'lb': 0.45359237,
        'ounce': 0.0283495231,
        'ounces': 0.0283495231,
        'oz': 0.0283495231,
        'ton': 1000.0,
        'tons': 1000.0,
    }

    VOLUME_FACTORS = {
        'liter': 1.0,
        'liters': 1.0,
        'l': 1.0,
        'milliliter': 0.001,
        'milliliters': 0.001,
        'ml': 0.001,
        'gallon': 3.78541,
        'gallons': 3.78541,
        'quart': 0.946353,
        'quarts': 0.946353,
        'pint': 0.473176,
        'pints': 0.473176,
        'cup': 0.236588,
        'cups': 0.236588,
        'fluid ounce': 0.0295735,
        'fluid ounces': 0.0295735,
        'fl oz': 0.0295735,
    }

    TIME_FACTORS = {
        'second': 1.0,
        'seconds': 1.0,
        's': 1.0,
        'minute': 60.0,
        'minutes': 60.0,
        'min': 60.0,
        'hour': 3600.0,
        'hours': 3600.0,
        'h': 3600.0,
        'day': 86400.0,
        'days': 86400.0,
        'week': 604800.0,
        'weeks': 604800.0,
    }

    TEMPERATURE_UNITS = ['celsius', 'fahrenheit', 'kelvin']

    def convert_length(self, value, from_unit, to_unit):
        f = self.LENGTH_FACTORS.get(from_unit.lower())
        t = self.LENGTH_FACTORS.get(to_unit.lower())
        if f is None or t is None:
            raise ValueError("Unsupported length unit.")
        return value * f / t

    def convert_mass(self, value, from_unit, to_unit):
        f = self.MASS_FACTORS.get(from_unit.lower())
        t = self.MASS_FACTORS.get(to_unit.lower())
        if f is None or t is None:
            raise ValueError("Unsupported mass unit.")
        return value * f / t

    def convert_volume(self, value, from_unit, to_unit):
        f = self.VOLUME_FACTORS.get(from_unit.lower())
        t = self.VOLUME_FACTORS.get(to_unit.lower())
        if f is None or t is None:
            raise ValueError("Unsupported volume unit.")
        return value * f / t

    def convert_time(self, value, from_unit, to_unit):
        f = self.TIME_FACTORS.get(from_unit.lower())
        t = self.TIME_FACTORS.get(to_unit.lower())
        if f is None or t is None:
            raise ValueError("Unsupported time unit.")
        return value * f / t

    def convert_temperature(self, value, from_unit, to_unit):
        fu = from_unit.lower()
        tu = to_unit.lower()
        if fu not in self.TEMPERATURE_UNITS or tu not in self.TEMPERATURE_UNITS:
            raise ValueError("Unsupported temperature unit.")

        # Convert from from_unit to Celsius
        if fu == 'celsius':
            c = value
        elif fu == 'fahrenheit':
            c = (value - 32) * 5.0 / 9.0
        elif fu == 'kelvin':
            c = value - 273.15

        # Convert from Celsius to to_unit
        if tu == 'celsius':
            return c
        elif tu == 'fahrenheit':
            return c * 9.0 / 5.0 + 32
        elif tu == 'kelvin':
            return c + 273.15

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        # Length
        if from_unit in self.LENGTH_FACTORS and to_unit in self.LENGTH_FACTORS:
            return self.convert_length(value, from_unit, to_unit)
        # Mass
        elif from_unit in self.MASS_FACTORS and to_unit in self.MASS_FACTORS:
            return self.convert_mass(value, from_unit, to_unit)
        # Volume
        elif from_unit in self.VOLUME_FACTORS and to_unit in self.VOLUME_FACTORS:
            return self.convert_volume(value, from_unit, to_unit)
        # Time
        elif from_unit in self.TIME_FACTORS and to_unit in self.TIME_FACTORS:
            return self.convert_time(value, from_unit, to_unit)
        # Temperature
        elif from_unit in self.TEMPERATURE_UNITS and to_unit in self.TEMPERATURE_UNITS:
            return self.convert_temperature(value, from_unit, to_unit)
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")


# Simple API function
_converter = UnitConverter()

def convert(value, from_unit, to_unit):
    """
    Convert value from from_unit to to_unit.
    Supported types: length, mass, volume, time, temperature.
    """
    return _converter.convert(value, from_unit, to_unit)
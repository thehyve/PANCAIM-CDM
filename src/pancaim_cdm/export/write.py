import json


class CustomJSONEncoder(json.JSONEncoder):
    """Custom "JSON" encoder writes the requested format.
    To use this encoder, use json.dump(data_dict, cls=CustomJSONEncoder)
    Based on: based on https://gist.github.com/jannismain/e96666ca4f059c3e5bc28abb711b5c92"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # config vars
        self.indentation_level = -1
        self.indent = 4

    def encode(self, o: dict) -> str:
        """This encodes the initial dictionary, and all non-empty dictionaries"""
        if not o:
            return ''

        self.indentation_level += 1

        output = []
        for k, v in o.items():
            if isinstance(v, (str, int, float)) or v is None:                   # to encode key-value pairs in one line (like table fields)
                output.append(self._encode_item(k, v))
            elif isinstance(v, dict) and len(v) == 0:                           # to encode empty dictionaries (like empty tables), including "None"
                output.append(self._encode_empty_dict(k))
            else:                                                               # to encode non-empty dictionaries
                output.append(
                    # f"{self.indent_str}{json.dumps(k)}\n{self.encode(v)}"     # to keep basic json format of using double quotes, uncomment this and comment line below
                    f"{self.indent_str}{k}\n{self.encode(v)}"
                )
        self.indentation_level -= 1
        return "\n".join(output)

    def _encode_empty_dict(self, k) -> str:
        """This encodes empty dictionaries (like empty tables)"""
        # return f"{self.indent_str}{json.dumps(k)}"                            # to keep basic json format of using double quotes, uncomment this and comment line below
        return f"{self.indent_str}{k}"

    def _encode_item(self, k, v) -> str:
        """This encodes key-value pairs in one line (like table fields), including 'None'"""
        # return f"{self.indent_str}{json.dumps(k)} = {self.encode(v)}"         # to keep basic json format of using double quotes, uncomment this and comment line below
        return f"{self.indent_str}{k} = {v}"

    def iterencode(self, o, **kwargs) -> str:
        """Required to also work with `json.dump`."""
        return self.encode(o)

    @property
    def indent_str(self) -> str:
        if self.indentation_level == 0:                                         # First level (tables)
            return ''
        elif isinstance(self.indent, int):                                      # Second level (items)
            return (" " * (self.indentation_level * self.indent)) + '- '
        elif isinstance(self.indent, str):                                      # Third level (fields)
            return (self.indentation_level * self.indent) + '- '
        else:                                                                   # Should not happen
            raise ValueError(f"indent must either be of type int or str (is: {type(self.indent)})")

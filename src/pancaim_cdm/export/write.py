import json


class CustomJSONEncoder(json.JSONEncoder):
    """Custom "JSON" encoder writes the requested format.
    Based on: based on https://gist.github.com/jannismain/e96666ca4f059c3e5bc28abb711b5c92"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # config vars
        self.indentation_level = -1
        self.indent = 4

    def encode(self, o) -> str:
        if isinstance(o, dict):
            return self._encode_object(o)

        return json.dumps(o)

    def _encode_object(self, o) -> str:
        if not o:
            return ''

        self.indentation_level += 1

        output = []
        for k, v in o.items():
            if isinstance(v, (str, int, float)) or v is None:
                output.append(self._encode_item(k, v))
            elif isinstance(v, dict) and len(v) == 0:
                output.append(self._encode_empty_dict(k))
            else:
                output.append(
                    # f"{self.indent_str}{json.dumps(k)}\n{self.encode(v)}"     # keeps basic json format of using double quotes
                    f"{self.indent_str}{k}\n{self.encode(v)}"
                )
        self.indentation_level -= 1
        return "\n".join(output)

    def _encode_empty_dict(self, k) -> str:
        # return f"{self.indent_str}{json.dumps(k)}"                            # keeps basic json format of using double quotes
        return f"{self.indent_str}{k}"

    def _encode_item(self, k, v) -> str:
        # return f"{self.indent_str}{json.dumps(k)} = {self.encode(v)}"         # keeps basic json format of using double quotes
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

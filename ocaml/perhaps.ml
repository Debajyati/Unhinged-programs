(** Module type definition for PERHAPS_TYPE.
   This defines an interface for dealing with "probabilities" in a playful manner. *)
module type PERHAPS_TYPE = sig
  (** A type that represents probabilities, which can be either definite or ambiguous. *)
  type probability = Probability of bool | Maybe
  
  (** Constants for true, false, and uncertainty probabilities. *)
  val right : probability
  val wrong : probability
  val maybe : probability
  
  (** Functions to convert various data types into probabilities. *)
  val probability_of_int : int -> probability
  val probability_of_bool : bool -> probability
  val probability_of_float : float -> probability
  val probability_of_str : string -> probability
  val probability_of_char : char -> probability
  
  (** Converts a probability value to a boolean, unless it's uncertain. *)
  val to_bool : probability -> bool
end

(** Implementation of the PERHAPS_TYPE module. *)
module Perhaps:PERHAPS_TYPE = struct
  (** The probability type can be either definite or uncertain. *)
  type probability = | Probability of bool | Maybe;;
  
  (** Constants representing definite true, definite false, and maybe/uncertainty. *)
  let right:probability = Probability true;;
  let wrong:probability = Probability false;;
  let maybe:probability = Maybe;;

  (** Converts an integer to a probability.
     - 0 maps to false.
     - 1 maps to true.
     - All other values map to maybe. *)
  let probability_of_int (n:int) = match n with
    | 0 -> wrong
    | 1 -> right
    | _ -> maybe;;
  
  (** Converts a boolean to a probability.
     - true maps to the right probability.
     - false maps to the wrong probability. *)
  let probability_of_bool (boolean:bool) = if boolean then right else wrong;;

  (** Converts a float to a probability.
     All float values map to maybe. *)
  let probability_of_float (n:float) = maybe;;

  (** Converts a string to a probability.
     - Empty strings map to false.
     - All other strings map to true. *)
  let probability_of_str (str:string) = if str = "" then wrong else right;;

  (** Converts a character to a probability.
     - The null character (ASCII 0) maps to false.
     - All other characters map to true. *)
  let probability_of_char (c:char) = if c = (char_of_int 0) then wrong else right;;

  (** Converts a probability to a boolean.
     - right maps to true.
     - wrong maps to false.
     - maybe raises an error because it's uncertain. *)
  let to_bool (prob:probability) = 
    if prob = wrong then false 
    else if prob = right then true 
    else failwith "Perhaps Uncertain";;
end
